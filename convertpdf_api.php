<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Convert</title>
</head>
<body>
    <?php

    $FileHandle = fopen('eto_na_yung_excel.pdf', 'w+');
    
    $curl = curl_init();
    
    $instructions = '{
      "parts": [
        {
          "file": "document"
        }
      ]
    }';
    
    curl_setopt_array($curl, array(
      CURLOPT_URL => 'https://api.pspdfkit.com/build',
      CURLOPT_CUSTOMREQUEST => 'POST',
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => '',
      CURLOPT_POSTFIELDS => array(
        'instructions' => $instructions,
        'document' => new CURLFILE('excel.xlsx')
      ),
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer pdf_live_fks3MaKwGQAaRm6H1atpHAGJalfmNAXLqorSmjhf6HX'
      ),
      CURLOPT_FILE => $FileHandle,
    ));
    
    $response = curl_exec($curl);
    
    curl_close($curl);
    
    fclose($FileHandle);
    
    
    ?>

</body>
</html>