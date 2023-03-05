<?php
// Check if the form has been submitted
if (isset($_POST['print_it'])){
  // Get the form data
  $color_mode = $_POST["color_mode"];
  $copies = $_POST["copies"];
  $paper_size = $_POST["paper_size"];

  // Store the uploaded PDF file on the server
  $target_dir = "uploads/";
  $target_file = $target_dir . basename($_FILES["pdf_file"]["name"]);
  move_uploaded_file($_FILES["pdf_file"]["tmp_name"], $target_file);

  // Call the Python script to print the document
  $command = "python printhings.py " . escapeshellarg($target_file) . " " . escapeshellarg($color_mode) . " " . escapeshellarg($copies) . " " . escapeshellarg($paper_size);
  exec($command);

  // Redirect the user to a success page
  header("Location: success.php");
  exit();
}
?>