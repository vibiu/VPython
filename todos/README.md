#运行
    python manage.py createall  //create database
    python manage.py runserver  //server start
    python manage.py dropall    //drop all database

#Users
##注册
    curl -H "Content-Type: application/json" -X POST -d '{"username":"pythonadmin","password":"123456"}' -i http://localhost:5000/api/1.0/users

#Todos
##增
    curl -u pythonadmin:123456 -H "Content-Type: application/json" -X POST -d '{"title":"about python", "body": "Beautiful is better than ugly"}' -i http://localhost:5000/api/1.0/todo/create

##删
    curl -u pythonadmin:123456 -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/api/1.0/todo/delete/<int:todo_id>

##查
    curl -u pythonadmin:123456 -H "Content-Type: application/json" -i http://localhost:5000/api/1.0/todos
    curl -u pythonadmin:123456 -H "Content-Type: application/json" -i http://localhost:5000/api/1.0/todo/<int:todo_id>

##改
    curl -u pythonadmin:123456 -H "Content-Type: application/json" -X PUT -d '{"body": "Simple is better than complex"}' -i http://localhost:5000/api/1.0/todo/put/<int:todo_id>

#url_map
    <Rule '/api/1.0/todo/create' (POST, OPTIONS) -> api.create_todo>,
    <Rule '/api/1.0/todos' (HEAD, OPTIONS, GET) -> api.get_todos>,
    <Rule '/api/1.0/users' (POST, OPTIONS) -> api.new_user>,
    <Rule '/api/1.0/todo/delete/<todo_id>' (OPTIONS, DELETE) -> api.delete_todo>,
    <Rule '/api/1.0/todo/put/<todo_id>' (PUT, OPTIONS) -> api.put_todo>,
    <Rule '/api/1.0/todo/<todo_id>' (HEAD, OPTIONS, GET) -> api.get_todo>,

<table>
    <tr>
        <th>method/url</th>
        <th>param</th>
        <th>return</th>
    </tr>
    <tr>
        <th><code>POST /api/1.0/users</code></th>
        <th><code>{"username":"pythonadmin","password":"123456"}</code></th>
        <th><code>{'username': "pythonadmin"}</code></th>
    </tr>
    <tr>
        <th><code>GET api/1.0/token</code></th>
        <th><code>None</code></th>
        <th><code>{
  "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1ODI2ODI4OSwiaWF0IjoxNDU4MjY3Njg5fQ.eyJpZCI6MX0.dQDKcvETNcKG02P_ntF30slgztnbN1EkknPopp4SKQE"
}</code></th>
    </tr>
    <tr>
        <th><code>POST /api/1.0/todo/create</code></th>
        <th><code>{"title":"about python", "body": "Beautiful is better than ugly"}</code></th>
        <th><code>
        {
          "author": "pythonadmin", 
          "body": "Beautiful is better than ugly", 
          "done": false, 
          "id": 1, 
          "title": "about python"
        }

</code></th>
    </tr>
    <tr>
        <th><code>DELETE /api/1.0/todo/delete/<todo_id></code></th>
        <th><code>None</code></th>
        <th><code>{"result": "Todo deleted."}</code></th>
    </tr>
    <tr>
        <th><code>PUT /api/1.0/todo/put/<todo_id></code></th>
        <th><code>{"body": "Simple is better than complex"}</code></th>
        <th><code>{'result': 'Put done.'}</code></th>
    </tr>
    <tr>
        <th><code>GET /api/1.0/todos</code></th>
        <th><code>None</code></th>
        <th><code>{
  "todos": [
    {
      "author": "pythonadmin", 
      "body": "Beautiful is better than ugly", 
      "done": false, 
      "id": 1, 
      "title": "about python"
    }, 
    {
      "author": "pythonadmin", 
      "body": "Simple is better than complex", 
      "done": false, 
      "id": 2, 
      "title": "about pythoner"]
}</code></th>
    </tr>
    <tr>
        <th>GET <code>/api/1.0/todo/<int:todo_id></code></th>
        <th><code>{
  "todo": {
    "author": "pythonadmin", 
    "body": "Beautiful is better than ugly", 
    "done": false, 
    "id": 1, 
    "title": "about python"
  }
}</code></th>
    </tr>
</table>
