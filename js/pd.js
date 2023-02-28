function countPages(url) {
  // Load the PDF file
  PDFJS.getDocument(url).then(function(pdf) {
    // Loop through each page
    var coloredPages = 0;
    var bwPages = 0;
    for (var i = 1; i <= pdf.numPages; i++) {
      // Get the page object
      pdf.getPage(i).then(function(page) {
        // Get the page's colorspace
        var colorspace = page.pageInfo.colorSpace;
        if (colorspace === 'DeviceGray') {
          bwPages++;
        } else {
          coloredPages++;
        }
      });
    }
    // Display the results
    console.log('Colored Pages: ' + coloredPages);
    console.log('Black and White Pages: ' + bwPages);
  });
}
countPages('License.pdf');
