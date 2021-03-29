document.addEventListener('DOMContentLoaded', function() {

    // add evetn listener to each send friend reqeust btn
    var sendbtns = document.querySelectorAll('.sendrequest');
    for (var i = 0; i < sendbtns.length; i++) {
        sendbtns[i].addEventListener('click', send_friend_request, false);
    }
})


function send_friend_request(evt) {
    console.log('red');
    const el = evt.target.parentElement;
    const user_id = parseInt(el.id.replace('like-',''));
    

    fetch(`/send_friend_request/${user_id}`).then(() => {
        el.innerHTML = `
        <button class="btn btn-light requestsent" disabled>Request Sent</button>
        `
    })
}