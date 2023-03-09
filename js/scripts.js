function printPDF() {
    var pdfFile = document.getElementById("pdf").files[0];
    var colorMode = document.getElementById("color-mode").value;
    var paperSize = document.getElementById("paper-size").value;
    var numCopies = document.getElementById("copies").valueAsNumber;
    if (pdfFile && colorMode && paperSize && numCopies) {
      var fileReader = new FileReader();
      fileReader.onload = function(event) {
        var pdfData = event.target.result;
        var printWindow = window.open('', '', 'width=800,height=600');
        printWindow.document.write('<html><head><title>Print Preview</title></head><body>');
        printWindow.document.write('<embed width="100%" height="100%" name="plugin" src="' + pdfData + '#toolbar=0&navpanes=0&scrollbar=0&view=FitH" type="application/pdf">');
        printWindow.document.write('</body></html>');
        printWindow.document.close();
        printWindow.focus();
        for (var i = 0; i < numCopies; i++) {
          printWindow.print();
        }
        printWindow.close();
      };
      fileReader.readAsDataURL(pdfFile);
    }
  }