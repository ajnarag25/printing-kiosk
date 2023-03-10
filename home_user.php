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
            <img src="assets/icons/USER.png" width="70" alt="">
            <h1 class="title-user">USER </h1>
            <h1 class="user-title">PLEASE SCAN YOUR I.D FIRST</h1>
            <br>
            <button class="btn btn-danger user-print-btn" onclick="window.print();">CLICK HERE TO SCAN NOW</button>
        </div>
      </div>

      <script src="js/jquery.js"></script>
      <script src="js/bootstrap.bundle.min.js"></script>
      <script src="js/functions.js"></script>
</body>
</html>