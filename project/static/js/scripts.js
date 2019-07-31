$(document).ready(function () {

    // Initialize Materialize Elements
    function initMaterialize() {
        $(".modal").modal();
        $(".tooltipped").tooltip();
        $(".sidenav").sidenav({edge: "right", draggable: true});
        $(".dropdown-trigger").dropdown();
        $("select").formSelect();
    }
    initMaterialize();

    // Custom 'Flash' Messages
    function flashToast() {
        $("#flashToast").addClass("show");
        setTimeout(function () {
            $("#flashToast").removeClass("show");
        }, 7500);
    }
    flashToast();

    // get current year for Copyright
    $("#year").html(new Date().getFullYear());
});
