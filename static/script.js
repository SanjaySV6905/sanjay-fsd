$(document).ready(function() {
    // Search functionality
    $('#searchInput').on('keyup', function() {
        let searchText = $(this).val().toLowerCase();
        let visibleCount = 0;
        
        $('.card').each(function() {
            let cardText = $(this).text().toLowerCase();
            
            if (cardText.includes(searchText)) {
                $(this).parent().show();
                visibleCount++;
            } else {
                $(this).parent().hide();
            }
        });
        
        if (visibleCount === 0 && searchText !== '') {
            $('#noResults').show();
        } else {
            $('#noResults').hide();
        }
    });
    
    // Form validation
    $('#recipeForm').on('submit', function(e) {
        let isValid = true;
        
        // Check if recipe name is empty
        if ($('#name').val().trim() === '') {
            alert('Please enter a recipe name');
            isValid = false;
            return false;
        }
        
        // Check if time is empty
        if ($('#time').val().trim() === '') {
            alert('Please enter cooking time');
            isValid = false;
            return false;
        }
        
        // Check if ingredients is empty
        if ($('#ingredients').val().trim() === '') {
            alert('Please enter ingredients');
            isValid = false;
            return false;
        }
        
        // Check if instructions is empty
        if ($('#instructions').val().trim() === '') {
            alert('Please enter instructions');
            isValid = false;
            return false;
        }
        
        if (isValid) {
            alert('Recipe added successfully!');
        }
    });
    
    // Add animation to cards
    $('.card').hide().fadeIn(1000);
    
    // Star rating system
    $('.star').on('click', function() {
        let rating = $(this).data('value');
        let form = $(this).closest('.rating-form');
        
        // Set the hidden input value
        form.find('.rating-value').val(rating);
        
        // Update visual feedback
        form.find('.star').removeClass('selected');
        form.find('.star').each(function() {
            if ($(this).data('value') <= rating) {
                $(this).addClass('selected');
            }
        });
        
        // Submit the form automatically
        form.submit();
    });
    
    // Hover effect for stars
    $('.star').on('mouseenter', function() {
        let rating = $(this).data('value');
        let form = $(this).closest('.rating-form');
        
        form.find('.star').removeClass('hover');
        form.find('.star').each(function() {
            if ($(this).data('value') <= rating) {
                $(this).addClass('hover');
            }
        });
    });
    
    $('.star-rating').on('mouseleave', function() {
        $(this).find('.star').removeClass('hover');
    });
});
