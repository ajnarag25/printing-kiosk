<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="assets/tup-logo.png" rel="icon">
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
        <div class="text-center header-space">
            <h1 class="title-user">Upload your file</h1>
            <br>
            <button class="img-upload" id="upload-img">
                <img src="assets/icons/UPLOAD.png" width="300" alt="">
            </button>
            <div class="input-hidden">
                <form id="upload-form" action="user_print.php" method="POST" enctype="multipart/form-data">
                    <input type="file" id="uploadfile" name="uploaded_file" /> 
                </form>

            </div>
            <h3>Click the icon to upload your file</h3>
        </div>
      </div>

    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/functions.js"></script>

</body>
</html>