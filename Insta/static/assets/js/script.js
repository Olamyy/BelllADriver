/**
 * Created by lekanterragon on 7/18/16.
 */

$('document').ready(function () {
       $('#book_form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        drivers();

});

    function drivers() {
        console.log('Drivers Book is working');
        console.log()
    }
});