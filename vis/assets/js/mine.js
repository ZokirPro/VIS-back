$(document).ready(function () {
        
        // Setup - add a text input to each footer cell
       
       
        // DataTable
        var table = $('#example').DataTable({
            columnDefs: [{
               targets: 0,
                checkboxes:{
                selectRow:true
                },
                className:'hello'
            }],
            select: {
                style: 'multi',
               
            },
            order: [[1, 'asc']]
        });



    });