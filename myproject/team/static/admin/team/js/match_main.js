$(document).ready(function(){
    $('#id_team_home').on('change', function(){
        $("#id_team_away option").show();
        if($(this).val() == $('#id_team_away').val()){
            $('#id_team_away').prop("selectedIndex", 0);
        }
        $('#id_team_away').children("option[value^=" + $(this).val() + "]").hide();
    });
});