;(function($) {
        $(window).load(function() {
            title = "{{ title }}"
            
            if(title == "Thank you"){
                $('#element_to_pop_up').bPopup({
                    speed: 650,
                    transition: 'slideDown',
                    transitionClose: 'slideBack'
                });
            }
            
         });
     })(jQuery);






