<?php  

if(isset($_POST['submit'])){
    $file =$_FILES['file'];
    #print_r($file);
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    $fileSize = $_FILES['file']['size'];
    $fileError = $_FILES['file']['error'];
    $fileType = $_FILES['file']['type'];

    $fileExt= explode('.', $fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('jpg', 'jpeg', 'png', 'pdf');

    if (in_array($fileActualExt, $allowed)){
        if($fileError === 0){
            if($fileSize< 1000000){
                
                $fileNameNew = "picture".".".$fileActualExt;
#uploding

                $fileDestination= 'uploads/'.$fileNameNew;
                move_uploaded_file($fileTmpName, $fileDestination);
                
                
                #echo "success";

                #activates the python code
                $command = escapeshellcmd('C:/xampp/htdocs/dingus.py');
                $output = shell_exec($command);
                echo $output;
                #sends back to index 
                echo "<script type='text/javascript'> window.location='index.php'; </script>";
               
                

            }else{
                echo "TOO GOSH DARN BIG";
            }
        }else{
            echo " THERE WAS AN ERROR UPLOADING STOOPID";
        }
    }else{
        echo "You cannot upload files of this type YA DINGUS";
    }

}
?>

