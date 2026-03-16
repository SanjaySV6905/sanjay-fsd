$(document).ready(function () {

    // Search - filter cards as user types
    $('#searchInput').on('keyup', function () {
        let text = $(this).val().toLowerCase();
        let count = 0;
        $('.card').each(function () {
            let match = $(this).text().toLowerCase().includes(text);
            $(this).parent().toggle(match);
            if (match) count++;
        });
        $('#noResults').toggle(count === 0 && text !== '');
    });

    // Star hover effect
    $('.star').on('mouseenter', function () {
        let val = $(this).data('value');
        $(this).closest('.star-rating').find('.star').each(function () {
            $(this).toggleClass('hover', $(this).data('value') <= val);
        });
    });
    $('.star-rating').on('mouseleave', function () {
        $(this).find('.star').removeClass('hover');
    });

    // Star click - set value and submit form
    $('.star').on('click', function () {
        let val = $(this).data('value');
        let form = $(this).closest('form');
        form.find('.rating-value').val(val);
        form.submit();
    });

    // Add recipe form validation
    $('#recipeForm').on('submit', function (e) {
        let fields = ['name', 'time', 'ingredients', 'instructions'];
        for (let field of fields) {
            if ($('#' + field).val().trim() === '') {
                alert('Please fill in: ' + field);
                e.preventDefault();
                return;
            }
        }
    });

});
