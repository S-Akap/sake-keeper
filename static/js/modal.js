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

function bottleDelete() {
    swalMixin.fire({
        title: '確認',
        text: 'このボトルを削除しますか？',
        color: "#1e3e61", // var(--color-primary1)
        background: "#dde7f5", // var(--color-white)
        showCancelButton: true,
        confirmButtonText: 'Delete',
        cancelButtonText: 'Back',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            document.querySelector("#bottle-delete-form").submit();
        }
    });
}

function bottleManagementDelete() {
    swalMixin.fire({
        title: '確認',
        text: 'この管理用IDを削除しますか？',
        color: "#1e3e61", // var(--color-primary1)
        background: "#dde7f5", // var(--color-white)
        showCancelButton: true,
        confirmButtonText: 'Delete',
        cancelButtonText: 'Back',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            document.querySelector("#bottle-management-delete-form").submit();
        }
    });
}

function bottleChangeIsEmpty(isEmpty) {
    let text;
    if (isEmpty == "False") {
        text = '[空ボトルか？]をNoからYesに変更しますか？'
    } else if (isEmpty == "True") {
        text = '[空ボトルか？]をYesからNoに変更しますか？'
    }
    swalMixin.fire({
        title: '確認',
        text: text,
        color: "#1e3e61", // var(--color-primary1)
        background: "#dde7f5", // var(--color-white)
        showCancelButton: true,
        confirmButtonText: 'Change',
        cancelButtonText: 'Back',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            document.querySelector("#bottle-change-is-empty-form").submit();
        }
    });
}