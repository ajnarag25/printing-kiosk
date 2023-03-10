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
        <div class="text-center header-space">
            <h1 class="title">Welcome! </h1>
            <div class="container mt-5">
                <div class="row">
                    <div class="col">
                        <div class="card card-custom">
                            <a href="home_user.php" data-bs-toggle="tooltip" data-bs-placement="top" title="User">
                                <h3><span><img src="assets/icons/USER.png" width="50" alt=""></span> USER</h3>
                            </a>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card card-custom">
                            <a href="login_admin.php" data-bs-toggle="tooltip" data-bs-placement="top" title="Admin">
                                <h3><span><img src="assets/icons/ADMIN.png" width="50" alt=""></span> ADMIN</h3>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>


    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/functions.js"></script>
</body>
</html>