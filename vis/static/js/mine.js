  // DataTable
    var table = $('#example').DataTable({
         
    "columnDefs" : [
        { targets: 0, sortable: false},
    ],
    "order": [[ 1, "asc" ]],
    
    });

 $('#checkall').click(function() {
  if ($(this).is(':checked')) {
    var checkboxes=document.querySelectorAll(".checkone")

    for(var i=0;i<checkboxes.length;i++)
    {
        checkboxes[i].checked =true
    }
  }
  else
  {
    var checkboxes=document.querySelectorAll(".checkone")
    for(var i=0;i<checkboxes.length;i++)
    {
        checkboxes[i].checked =false
    }
  } 
});

var need_remove=document.querySelectorAll("#remove_class")
need_remove[0].removeClass('sorting_asc')