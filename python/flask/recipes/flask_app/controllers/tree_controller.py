from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app.models import tree_model, user_model
from flask_app.models.tree_model import Tree
from flask_app.models.user_model import User

# CREATE ADVENTURE CONTROLLER
@app.route('/tree/create', methods=['GET'])
def create_page():
    user_id = session.get('user_id')  # Fetch user ID from session
    if user_id is None:
        flash('User not logged in')
        return redirect('/')
    return render_template('create_tree.html')



@app.route('/tree/create', methods=['POST'])
def create_tree():
    if Tree.create_trees(request.form):
        return redirect('/users/home')
    else:
        flash('Error creating tree')
        return redirect('/tree/create')



#------------------- SECTION CHANGE ---------------#


# READ TREE CONTROLLER
@app.route('/tree/view/<int:tree_id>')
def view_tree(tree_id):
    if 'user_id' not in session:
        flash('Login to view this page')
        session.clear()
        return redirect('/')

    user_id = session['user_id']

    # Use the Tree class method to get all trees with hosts
    trees = Tree.get_all_trees_W_hosts()

    # Find the selected tree by matching the tree_id
    selected_tree = next((tree for tree in trees if tree.id == tree_id), None)

    if selected_tree:
        return render_template('view_singular_tree.html', tree=selected_tree)
    else:
        flash('Tree not found')
        return redirect('/')





#------------------- SECTION CHANGE ---------------#


# -@@@@@ UPDATE Tree PAGE @@@@@@-
@app.route('/tree/edit/<int:tree_id>', methods=['GET'])
def show_edit_tree(tree_id):
    if 'user_id' not in session:
        flash('Login to view this page')
        session.clear()
        return redirect('/')

    data = {
        'id': tree_id
    }

    current_user_trees = Tree.get_trees_for_user(session['user_id'])

    tree = Tree.read_one_tree(data)

    return render_template('edit_tree.html', tree=tree, current_user_trees=current_user_trees)

#! Route to update a single tree
@app.route('/tree/edit/<int:tree_id>', methods=['POST'])
def update_single_tree(tree_id):
    tree_data = {
        'id': tree_id,
        'user_id': session['user_id'],
        'specie': request.form['specie'],
        'location': request.form['location'],
        'date_found': request.form['date_found'],
        'zip': request.form['zip'],
        'note': request.form['note']
    }

    if not tree_data['specie'] or not tree_data['location'] or not tree_data['date_found'] or not tree_data['zip'] or not tree_data['note']:
        flash('All fields are required.', 'update_tree')
        return redirect(url_for('show_edit_tree', tree_id=tree_id))

    Tree.update_tree(tree_data)
    flash('Tree updated successfully', 'success')
    return redirect('/users/home')




@app.route('/purchase/tree/<int:tree_id>', methods=['POST'])
def update_tree(tree_id):
    tree_data = {
        'id': tree_id,
        'user_id': session['user_id'],
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity']
    }




#------------------- SECTION CHANGE ---------------#





# DELETE ADVENTURE CONTROLLER
# DELETE ADVENTURE CONTROLLER
# DELETE ADVENTURE CONTROLLER
@app.route('/tree/delete/<int:tree_id>')
def delete_tree(tree_id):
    # Check if the user is logged in
    if 'user_id' not in session:
        flash('Login to view this page')
        session.clear()
        return redirect('/')

    this_tree = {
        'id': tree_id,
        'user_id': session['user_id']
    }

    Tree.delete_tree(this_tree)

    return redirect('/users/home')


#------------------- SECTION CHANGE ---------------#



# Route to display tree details and purchase button
@app.route('/tree/view/<int:tree_id>', endpoint='view_single_tree')
def view_tree(tree_id):
    if 'user_id' not in session:
        flash('Login to view this page')
        session.clear()
        return redirect('/')

    user_id = session['user_id']

    current_user = User.get_user_by_id(user_id)  # Assuming you have a method to get user by ID

    trees = Tree.get_all_trees_W_hosts()
    selected_tree = next((tree for tree in trees if tree.id == tree_id), None)

    if selected_tree:
        return render_template('view_singular_tree.html', tree=selected_tree, current_user=current_user)
    else:
        flash('Tree not found')
        return redirect('/')







# Route to handle tree purchase
@app.route('/tree/purchase/<int:tree_id>', methods=['POST'])
def purchase_tree(tree_id):
    if 'user_id' not in session:
        flash('Login to make a purchase', 'error')
        return redirect('/')

    amount_purchased = request.form['amount_purchased']

    if amount_purchased and amount_purchased.isdigit():
        quantity_to_purchase = int(amount_purchased)
    else:
        flash('Please enter a valid quantity for purchase', 'error')
        return redirect('/tree/view/{}'.format(tree_id))

    tree = Tree.read_one_tree({'id': tree_id})

    purchase_information = {
        'title': tree.title,
        'description': tree.description,
        'price': tree.price,
        'quantity': tree.quantity - quantity_to_purchase,
        'id': tree.id
    }

    if tree.quantity < quantity_to_purchase:
        flash('Not enough stock available', 'error')
        return redirect('/tree/view/{}'.format(tree_id))

    # Perform the purchase and update quantity
    Tree.update_tree(purchase_information)

    flash(f'You successfully purchased {quantity_to_purchase} units of "{tree.title}"', 'success')
    return redirect('/tree/view/{}'.format(tree_id))
