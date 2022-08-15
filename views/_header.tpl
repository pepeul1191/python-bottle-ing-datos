<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="/favicon.png" />
  <title>{{locals['title']}}</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
<ul>
% for item in locals['menu']:
  % if item['active'] == True: 
    <li><a class="active" href="{{item['url']}}">{{item['name']}}</a></li>
  % else:
    <li><a href="{{item['url']}}">{{item['name']}}</a></li>
  % end
% end
</ul>
<div id="app-container">