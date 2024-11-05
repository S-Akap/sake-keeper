const swalMixin = Swal.mixin({
    customClass: {
      confirmButton: "btn modal-btn",
      cancelButton: "sub-btn modal-btn"
    },
    buttonsStyling: false
});

function sampleLogin() {
    swalMixin.fire({
        title: '確認',
        text: 'Sample Accountでログインしますか？',
        color: "#1e3e61", // var(--color-primary1)
        background: "#dde7f5", // var(--color-white)
        showCancelButton: true,
        confirmButtonText: 'Log In',
        cancelButtonText: 'Back',
        reverseButtons: true
    }).then((result) => {
    if (result.isConfirmed) {
        window.location.href = "/account/sample-login/";
    }
    });
}

