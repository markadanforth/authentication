% rebase('template.tpl', title='signin')

<h1>signin</h1>

<form method="post" action="/signin">
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

    <input class="btn btn-primary" type="submit" value="Submit">
</form>