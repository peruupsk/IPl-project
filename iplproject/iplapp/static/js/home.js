document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("playerForm").addEventListener("submit", function(event) {
        event.preventDefault();
        let name = document.getElementById("playerName").value;
        let team = document.getElementById("playerTeam").value;

        if(name.trim() === "") {
            alert("Please enter a player name!");
            return;
        }

        alert(`Player ${name} added to ${team}!`);
    });
});
