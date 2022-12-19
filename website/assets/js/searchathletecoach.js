
function fetchathletes(name='') {
  document.getElementById("list_athletes").innerHTML = "loading...";
  fetch(`/athletes?name=${name}`)
    .then(response => response.json())
    .then(data => {

      document.getElementById("list_athletes").innerHTML = "";
      if (data.length === 0) {
        document.getElementById("list_athletes").innerHTML = "No athletes found";
      }
      data.forEach((player)=>{
    document.getElementById("list_athletes").innerHTML += `<div class="preview-item border-bottom">
      ${
        player.status === "Cleared" ? (' <td> <div class="badge badge-outline-success" > Cleared </div></td>') : player.status === "Partially Cleared" ? '<td> <div class="badge badge-outline-warning" > Partially Cleared </div></td>' : '<td> <div class="badge badge-outline-danger" > Not Cleared </div></td>'
    }
    <div class="preview-item-content d-flex flex-grow">
        <div class="flex-grow">
            <div class="d-flex d-md-block d-xl-flex justify-content-between">
                <a class="nav-link" href="athletepermissions.html/${player.user_id}"> ${player.Name} </a>

            </div>

        </div>
    </div>
</div>`

})
    });
}


function fetchacoaches(name='') {
  document.getElementById("list_coaches").innerHTML = "loading...";
  fetch(`/coaches?name=${name}`)
    .then(response => response.json())
    .then(data => {

      document.getElementById("list_coaches").innerHTML = "";
      if (data.length === 0) {
        document.getElementById("list_coaches").innerHTML = "No coaches found";
      }
      data.forEach((coach)=>{
    document.getElementById("list_coaches").innerHTML += `<div class="preview-item border-bottom">
<div class="preview-item-content d-flex flex-grow">
  <div class="flex-grow">
    <div class="d-flex d-md-block d-xl-flex justify-content-between">
      <a class="nav-link" href="coachpermissions.html/${coach.user_id}"> ${coach.Name} </a>

    </div>

  </div>
</div>
</div>`

})
    });
}


  window.addEventListener('DOMContentLoaded', () => {

    fetchathletes();
     document.getElementById('search-athlete-button').addEventListener('click', () => {
      const name = document.getElementById('search-athlete-input').value;
      fetchathletes(name);
    });
    fetchacoaches();
     document.getElementById('search-coach-button').addEventListener('click', () => {
      const name = document.getElementById('search-coach-input').value;
      fetchacoaches(name);
    });


    });
