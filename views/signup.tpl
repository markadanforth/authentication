% rebase('template.tpl', title='join')

<h1>signup</h1>

<form method="post" action="/signup">
    <div class="form-group">
    <input type="text" 
           name="firstname" 
           required minlength="3"
           pattern="\S+"
           title="this field is required"
           placeholder="enter first name"></div>

    <div class="form-group">
    <input type="text" 
           name="lastname" 
           required minlength="3"
           pattern="\S+"
           title="this field is required"
           placeholder="enter last name"></div>

    <div class="form-group">
    <input type="email" 
           name="email" 
           required minlength="3"
           pattern="\S+"
           title="this field is required"
           placeholder="enter email"></div>

    <div class="form-group">
    <input type="password" 
           name="password" 
           required minlength="3"
           pattern="\S+"
           title="this field is required"
           placeholder="enter password"></div>

    <div class="form-group">
    <input type="password" 
           name="password2" 
           required minlength="3"
           pattern="\S+"
           title="this field is required"
           placeholder="enter password again"></div>
    <input class="btn btn-primary" type="submit" value="Submit">
</form>