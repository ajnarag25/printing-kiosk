<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="assets/tup-logo.png " rel="icon">
    <title>Printing Kiosk</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/custom_style.css">
</head>
<body>
    <div class="p-5">
        <div class="navbar">
            <h3><?php echo  date("l, F d, Y") ?></h3>
            <div class="d-flex">
                <h3>
                    <span id="LiveTime" class=""></span>
                </h3>
            </div>
        </div>
        <a href="index.php" data-bs-toggle="tooltip" data-bs-placement="top" title="Back">
            <img src="assets/icons/BACK.png" width="50" alt="">
        </a>
        <?php 
        if(isset($_FILES["uploaded_file"])) {
            $targetDir = "uploads/";
            $targetFile = $targetDir . basename($_FILES["uploaded_file"]["name"]);
            $uploadOk = 1;
            $fileType = strtolower(pathinfo($targetFile,PATHINFO_EXTENSION));
        
            // Check if file already exists
            if (file_exists($targetFile)) {
                echo "Sorry, file already exists.";
                $uploadOk = 0;
            }
        
            // Check file size
            if ($_FILES["uploaded_file"]["size"] > 500000) {
                echo "Sorry, your file is too large.";
                $uploadOk = 0;
            }
        
            // Allow certain file formats
            if($fileType != "jpg" && $fileType != "png" && $fileType != "jpeg"
            && $fileType != "gif" ) {
                echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
                $uploadOk = 0;
            }
        
            // Check if $uploadOk is set to 0 by an error
            if ($uploadOk == 0) {
                echo "Sorry, your file was not uploaded.";
            // if everything is ok, try to upload file
            } else {
                if (move_uploaded_file($_FILES["uploaded_file"]["tmp_name"], $targetFile)) {
                    echo "The file ". basename( $_FILES["uploaded_file"]["name"]). " has been uploaded.";
                } else {
                    echo "Sorry, there was an error uploading your file.";
                }
            }
        }
        ?>
        
        <div class="text-center header-space">
            <img src="assets/icons/LOAD SOME PAPER.png" width="150" alt="">
            <h1 class="title-user">Load some paper</h1>
            <h1 class="user-print">PLEASE LOAD ONLY ONE SIZE AND TYPE OF PAPER IN THE TRAY ONE AT A TIME.</h1>
            <br>
            <button class="btn btn-success user-print-btn">PROCEED</button>
        </div>
      </div>


    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/functions.js"></script>

</body>
</html>