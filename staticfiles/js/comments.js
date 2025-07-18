function showApprovalMessage() {
  var approvalModal = new bootstrap.Modal(document.getElementById('approvalModal'));
  approvalModal.show();
}

// Function to show Django-style messages
function showMessage(message, type) {
  const messageContainer = document.getElementById('message-container');
  if (!messageContainer) {
    // Create message container if it doesn't exist
    const container = document.createElement('div');
    container.id = 'message-container';
    container.className = 'container mt-3';
    document.body.insertBefore(container, document.body.firstChild);
  }
  
  const alertClass = type === 'error' ? 'alert-danger' : 'alert-success';
  const alertHtml = `
    <div class="alert ${alertClass} alert-dismissible fade show" role="alert">
      ${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  `;
  
  document.getElementById('message-container').innerHTML = alertHtml;
  
  // Auto-hide the message after 5 seconds
  setTimeout(() => {
    const alert = document.querySelector('.alert');
    if (alert) {
      alert.classList.remove('show');
      setTimeout(() => alert.remove(), 150);
    }
  }, 5000);
}

// Edit Comment
document.querySelectorAll('.btn-edit').forEach(item => {
  item.addEventListener('click', event => {
    const commentId = item.getAttribute('data-comment-id');
    const comment = document.querySelector(`#comment${commentId}`);
    const commentText = comment.innerText.trim();
    const rating = document.querySelector(`#rating${commentId}`).querySelectorAll('.fas').length;
    const edit_comment_url = "{% url 'edit_comment' post.pk 0 %}".replace('0', commentId);
    const form = `
      <form id="edit_comment_form_${commentId}" method="POST" action="${edit_comment_url}">
        {% csrf_token %}
        <input type="hidden" name="comment_id" value="${commentId}">
        <textarea name="text" class="form-control">${commentText}</textarea>
        <label for="rating">Rating:</label>
        <div class="star-rating">
          ${[1, 2, 3, 4, 5].map(i => `
            <i class="${i <= rating ? 'fas' : 'far'} fa-star text-warning" data-rating="${i}"></i>
          `).join('')}
        </div>
        <input type="hidden" name="rating" value="${rating}">
        <button type="submit" class="btn btn-primary mt-2">Save</button>
      </form>
    `;
    comment.innerHTML = form;

    document.querySelectorAll(`#edit_comment_form_${commentId} .fa-star`).forEach(star => {
      star.addEventListener('click', function() {
        const rating = this.getAttribute('data-rating');
        document.querySelector(`#edit_comment_form_${commentId} input[name="rating"]`).value = rating;
        document.querySelectorAll(`#edit_comment_form_${commentId} .fa-star`).forEach(s => {
          s.classList.remove('fas');
          s.classList.add('far');
        });
        for (let i = 1; i <= rating; i++) {
          document.querySelector(`#edit_comment_form_${commentId} .fa-star[data-rating="${i}"]`).classList.remove('far');
          document.querySelector(`#edit_comment_form_${commentId} .fa-star[data-rating="${i}"]`).classList.add('fas');
        }
      });
    });

    document.querySelector(`#edit_comment_form_${commentId}`).addEventListener('submit', function(e) {
      e.preventDefault();
      const formData = new FormData(this);
      fetch(edit_comment_url, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          comment.innerHTML = `<p>${data.text}</p>`;
          const ratingDiv = document.querySelector(`#rating${commentId}`);
          ratingDiv.innerHTML = '';
          for (let i = 1; i <= data.rating; i++) {
            ratingDiv.innerHTML += '<i class="fas fa-star text-warning"></i>';
          }
          for (let i = data.rating + 1; i <= 5; i++) {
            ratingDiv.innerHTML += '<i class="far fa-star text-warning"></i>';
          }
          // Show success message using Django messages
          showMessage('Comment updated successfully and is awaiting approval', 'success');
        } else {
          showMessage('Error in updating comment', 'error');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        showMessage('Error in updating comment', 'error');
      });
    });
  });
});

// New Comment Rating
document.querySelectorAll('#new_comment_rating .fa-star').forEach(star => {
  star.addEventListener('click', function() {
    const rating = this.getAttribute('data-rating');
    document.querySelector('#new_comment_rating_value').value = rating;
    document.querySelectorAll('#new_comment_rating .fa-star').forEach(s => {
      s.classList.remove('fas');
      s.classList.add('far');
    });
    for (let i = 1; i <= rating; i++) {
      document.querySelector(`#new_comment_rating .fa-star[data-rating="${i}"]`).classList.remove('far');
      document.querySelector(`#new_comment_rating .fa-star[data-rating="${i}"]`).classList.add('fas');
    }
  });
});
document.querySelector("#id_rating").style.display = "none";