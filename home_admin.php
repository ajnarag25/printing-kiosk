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
        <a href="login_admin.php" data-bs-toggle="tooltip" data-bs-placement="top" title="Logout">
            <img src="assets/icons/LOGOUT.png" width="50" alt="">
        </a>
        <div class="text-center mt-5">
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                          <h3 class="card-title">PRICE SETTINGS</h3>
                        </div>
                       <div class="card-content">
                           <h4 class="mt-2">BLACK : <span><a href=""><img src="assets/icons/MINUS.png" width="20" alt=""></span></a>  <input type="text" class="w-25 text-center" id="black_display" disabled>   <a type="button" onclick="addblack()"><span><img src="assets/icons/PLUS.png" width="20" alt=""></span></a></h4>
                           <h4 class="mt-2">COLORED : <span><a href=""><img src="assets/icons/MINUS.png" width="20" alt=""></span></a>  <input type="text" class="w-25 text-center" id="black_display" disabled>   <a type="button" onclick="addblack()"><span><img src="assets/icons/PLUS.png" width="20" alt=""></span></a></h4>
                            <div class="text-center mt-4">
                                <button class="btn btn-success">SAVE</button>
                                <button class="btn btn-danger">CANCEL</button>
                            </div>
                       </div>
                      </div>
                </div>
                <div class="col">
                    <div class="card-body">
                        <h3 class="card-title">PASSWORD SETTINGS</h3>
                    </div>
                    <div class="card-content">
                        <form action="">
                            <div class="input-group" id="show_hide_password">
                                <input class="form-control custom-input" id="result" type="password" placeholder="Password" disabled required>      
                                <a href="" data-bs-toggle="tooltip" data-bs-placement="top" title="Toggle Password" style="text-align: none; color: black;"> <img id="closed_eye" style="display:none" src="assets/icons/CLOSED_EYE.png"  width="20" alt=""> <img id="open_eye" src="assets/icons/OPEN_EYE.png" width="20" alt=""></a>
                            </div>
                            <center>
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
                                        <td> <input class="btn btn-success buttons" type="submit" value="SAVE" onclick="calculate()" id="btn" /> </td>
                                        <td> <input class="btn btn-danger buttons" type="button" value="CLEAR" onclick="clearScreen()" /> </td>
                                    </tr>
                                </table>
                            </center>
                        </form>
                
                
                    </div>
                </div>
                <div class="col">
                    <div class="card-body">
                        <h3 class="card-title">TIMER SETTINGS</h3>
                    </div>
                    <div class="card-content">
                        <h4 class="mt-4">TIME (SEC) : <span><a href=""><img src="assets/icons/MINUS.png"  width="20" alt=""></span></a>  <input type="text" class="w-25 text-center" id="black_display" disabled>   <a type="button" onclick="addblack()"><span><img src="assets/icons/PLUS.png" width="20" alt=""></span></a></h4>
                        <br>
                         <div class="text-center mt-4">
                             <button class="btn btn-success">SAVE</button>
                             <button class="btn btn-danger">CANCEL</button>
                         </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="admin_buttons">
                <button class="btn btn-warning" >PREVIEW RECORD DATA</button>
                <button class="btn btn-success">DOWNLOAD RECORD DATA</button>
                <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal">SHUTDOWN</button>
            </div>
      
  
            <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header" style="background-color: rgb(184, 49, 49); color: white;">
                    <h3>System Shutdown</h3>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="text-center">
                            <h1>Confirm <br> SHUTDOWN?</h1>
                        </div>
                    </div>
                    <div class="modal-footer">
                    <button type="button" class="btn btn-danger">YES</button>
                    <button type="button" class="btn btn-success" data-bs-dismiss="modal">BACK</button>
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