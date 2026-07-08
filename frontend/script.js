const API = "http://127.0.0.1:8000";


async function loadMedicines() {

    const response = await fetch(
        `${API}/medicines`
    );

    const medicines = await response.json();

    const medicineList =
        document.getElementById("medicineList");


    medicineList.innerHTML = "";


    medicines.forEach((medicine) => {

        medicineList.innerHTML += `

        <div class="medicine-card">

            <h3>${medicine.name}</h3>

            <p>Dosage: ${medicine.dosage}</p>

            <p>Time: ${medicine.time}</p>

            <button onclick="markTaken(${medicine.id}, this)">
                ${medicine.taken ? "✅ Taken" : "Mark Taken"}
            </button>

        </div>

        `;

    });

}



window.onload = loadMedicines;
async function addMedicine() {

    const name =
        document.getElementById("medicineName").value;

    const dosage =
        document.getElementById("dosage").value;

    const time =
        document.getElementById("time").value;


    const response = await fetch(
        `${API}/medicines`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                name: name,
                dosage: dosage,
                time: time,
                user_id: 1

            })
        }
    );


    if(response.ok){

        alert("Medicine added");

        loadMedicines();

    }

}
function checkReminder() {

    const now = new Date();

    const currentTime =
        now.toTimeString().slice(0,5);


    const medicines =
        document.querySelectorAll(".medicine-card");


    medicines.forEach((card)=>{

        const text = card.innerText;


        if(text.includes(currentTime)){

            const name =
            card.querySelector("h3").innerText;
            const audio = new Audio(
    "https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg"
);

            audio.volume = 0.4;
            audio.play();

            alert(
    "🔔 Medicine Reminder\n\n💊 " +
    name +
    "\n\nPlease take your medicine."
);
        }

    });

}
setInterval(
    checkReminder,
    10000
);
