% rebase('template.tpl', title='profile')

<h1>Welcome to the profile page</h1>

<p>This could be a awesome. Many friends. Many messages.</p>

<ul>
    <li>your id is: {{user['id']}}</li>
    <li>your first name is: {{user['firstname']}}</li>
    <li>your last name is: {{user['lastname']}}</li>
    <li>your email is: {{user['email']}}</li>
</ul>