$(document).ready(function() {


    // prevent form from refreshing by removing default and creating manual ajax post
    $('#new-post-form').submit(function(e) {
        $.post('/billboardapp/addpost', $(this).serialize(), function(data){
            console.log(data.message);
        });
        e.preventDefault();
    });

    // prevent default for sending comments
    $('.post-comment-form').submit(function(e) {
    
        var dataform = $(this).serialize().concat('&postnumber=');
        dataform =  dataform.concat($(this).attr('alt'));
  
        $.post('/billboardapp/addcomment',dataform, function(data){
            console.log(data.message);
        });
        e.preventDefault();
        location.reload();
    });

    // Attache actions to button
    $("#button-confirm").click(function() {
        
        // post form
        $('#new-post-form').submit();
       
        $('#confirm-message-container').slideUp();
        $('#input-container').slideUp();
        $('#addmessage-container').slideDown();
        location.reload();
    });

    // hide input and confirm cells
    $('#input-container').hide();
    $('#confirm-message-container').hide();

    // add event listener to add message
    $("#button-add").click(function() {
        $('#input-container').slideDown();
        $('#confirm-message-container').slideDown();
        $('#addmessage-container').hide();
    });

    // add event listener to cancel input
    $('#button-cancel').click(function() {
        $('#confirm-message-container').slideUp();
        $('#input-container').slideUp();
        $('#addmessage-container').slideDown();
    })

    // add event listener to delete button (post)
    $('.delete-container').css( 'cursor', 'pointer' );
    $(".delete-container").click(function(){
        var postId = $(this).attr("alt");
        deletePost(postId);
    });

    // add event listener to delete button (comment)
    $('.delete-button').css( 'cursor', 'pointer' );
    $(".delete-button").click(function(){
        var commentId = $(this).attr("alt");
        deleteComment(commentId);
    });


    // show button submit comment
    $(".submit-comment-button").show();

    // hide helptext for register user
    $('.helptext').hide();


});


// delete a specific post
function deletePost(postId){
    console.log(postId);
    
    $.post( '/billboardapp/delpost', { postid: postId }, function( data ) {
            console.log("complete");
        }, "json");

    location.reload();
};


// delete a specific post
function deleteComment(commentId){
    console.log(commentId);
    
    $.post( '/billboardapp/delcomment', { commentid: commentId }, function( data ) {
            console.log("complete");
        }, "json");

    location.reload();

};