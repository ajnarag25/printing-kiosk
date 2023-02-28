<?php
// Load the TCPDF library
require_once('tcpdf/tcpdf.php');

// Load the PDF file
$pdfUrl = 'C:/Users/admin/Downloads/License.pdf';
$pdf = new TCPDF('P', 'pt', 'A4', true, 'UTF-8', false);
$pdf->setSourceFile($pdfUrl);

// Define counters for black and white pages and colored pages
$blackAndWhiteCount = 0;
$coloredCount = 0;

// Iterate over each page in the PDF
$numPages = $pdf->numPages;
for ($i = 1; $i <= $numPages; $i++) {
  // Add the page to the PDF object
  $pdf->AddPage();

  // Import the page from the PDF file
  $templateId = $pdf->importPage($i);

  // Determine whether the page is black and white or colored
  $pixels = $pdf->getImagePixels($templateId, 0, 0, -1, -1, false);
  $coloredPixels = 0;
  $blackAndWhitePixels = 0;
  foreach ($pixels as $pixel) {
    $r = $pixel[0];
    $g = $pixel[1];
    $b = $pixel[2];
    if ($r !== $g || $g !== $b) {
      $coloredPixels++;
    } else {
      $blackAndWhitePixels++;
    }
  }
  $isBlackAndWhite = ($coloredPixels / ($coloredPixels + $blackAndWhitePixels)) < 0.01;
  if ($isBlackAndWhite) {
    $blackAndWhiteCount++;
  } else {
    $coloredCount++;
  }

  // Output the page to a buffer and discard it
  $pdf->useTemplate($templateId, 0, 0, 0, 0, true, null, false);
  ob_start();
  $pdf->Output('dummy.pdf', 'I');
  ob_end_clean();
}

// Output the results
echo "Black and white pages: $blackAndWhiteCount\n";
echo "Colored pages: $coloredCount\n";

?>