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
            <img src="assets/icons/ADMIN.png" width="70" alt="">
            <h1 class="title-admin">Admin </h1>
            <div class="container mt-5 w-50">
                <form action="home_admin.php">
                    <div class="input-group" id="show_hide_password">
                        <input class="form-control custom-input" id="result" type="password" placeholder="Password" disabled required>      
                        <a href="" data-bs-toggle="tooltip" data-bs-placement="top" title="Toggle Password" style="text-align: none; color: black;"> <img id="closed_eye" style="display:none" src="assets/icons/CLOSED_EYE.png" width="20" alt=""> <img id="open_eye" src="assets/icons/OPEN_EYE.png" width="20" alt=""></a>
                    </div>
                   
                        <table class="calculator mt-5" >
                            <tr>
                                <td> <input class="btn btn-secondary buttons" type="button" value="1" onclick="display('1')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="2" onclick="display('2')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="3" onclick="display('3')" /> </td>
                            </tr>
                            <tr>
                                <td> <input class="btn btn-secondary buttons" type="button" value="4" onclick="display('4')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="5" onclick="display('5')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="6" onclick="display('6')" /> </td>
                            </tr>
                            <tr>
                                <td> <input class="btn btn-secondary buttons" type="button" value="7" onclick="display('7')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="8" onclick="display('8')" /> </td>
                                <td> <input class="btn btn-secondary buttons" type="button" value="9" onclick="display('9')" /> </td>
                            </tr>
                            <tr>
                                <td> <input class="btn btn-secondary buttons" type="button" value="0" onclick="display('0')" /> </td>
                                <td> <input class="btn btn-success buttons" type="submit" value="Enter" onclick="calculate()" id="btn" /> </td>
                                <td> <input class="btn btn-danger buttons" type="button" value="Clear" onclick="clearScreen()" /> </td>
                            </tr>
                        </table>
                
                </form>
            </div>
        </div>
      </div>


    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/functions.js"></script>

</body>
</html>