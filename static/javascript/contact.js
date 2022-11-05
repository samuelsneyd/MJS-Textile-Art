document.addEventListener('DOMContentLoaded', () => {
  const sendEmailButton = document.getElementById('send-email-button');
  const sendingAlert = document.getElementById('sending');
  const errorAlert = document.getElementById('error');
  const successAlert = document.getElementById('success');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const messageInput = document.getElementById('message');
  const alerts = [sendingAlert, errorAlert, successAlert];
  const inputFields = [nameInput, emailInput, messageInput, sendEmailButton];
  const csrftoken = getCookie('csrftoken');

  sendEmailButton.onclick = () => {
    const name = nameInput?.value?.trim();
    const email = emailInput?.value?.trim();
    const message = messageInput?.value?.trim();

    if (isEmailValid(name, email, message)) {
      sendingAlert.classList.remove('hidden');
      errorAlert.classList.add('hidden');
      successAlert.classList.add('hidden');

      inputFields.forEach((ele) => {
        ele.setAttribute('disabled', 'true');
      });

      fetch('/emails/email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
        credentials: 'same-origin',
        body: JSON.stringify({ email, name, message })
      }).then(response => response.json())
        .then(data => {
          if (data.status === 201) {
            nameInput.value = '';
            emailInput.value = '';
            messageInput.value = '';
            successAlert.classList.remove('hidden');
          } else {
            errorAlert.classList.remove('hidden');
          }
        })
        .catch(() => {
          errorAlert.classList.remove('hidden');
        })
        .finally(() => {
          sendingAlert.classList.add('hidden');
          inputFields.forEach((ele) => {
            ele.removeAttribute('disabled');
          });
        });
    } else {
      errorAlert.classList.remove('hidden');
    }
  };

  alerts.forEach((alert) => {
    alert.onclick = () => {
      alert.classList.add('hidden');
    };
  });

});

const isEmailValid = (name, email, message) => {
  return (
    name?.length > 0
    && email?.length > 0
    && (/\S+@\S+\.\S+/).test(email)
    && message?.length > 0
  );
};

const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};
