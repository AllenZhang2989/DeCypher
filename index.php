<!DOCTYPE html>
<html>
  <head>
    <title>DeCypher</title>
  </head>
  <body >
    <style> 
    body{
      background-image: url('bground.jpg');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: 160% 103%;
    }
    </style>
    <div>
      <img src="logo.png" style width="330" height ="200"/>
    </div>
    
    <form action="upload.php" method="POST" enctype="multipart/form-data">
      <input type="file" name="file" /> 
      <button type="submit" name="submit">UPLOAD</button>

    </form>
          <?php
              #activates the python code
              $command = escapeshellcmd('C:/xampp/htdocs/text_out.py');
              $output = shell_exec($command);
              echo $output;
          ?>
  </body>
</html>
