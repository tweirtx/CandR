function addDay() {
    var days = document.getElementById('teams');
    var html =
        `<br>
            <label>Team Number:
                <input type="text" pattern="\\d{1,5}">
            </label>
            <br>
                <label>Team Type:
                    <select>
                        <option value="fll">FLL</option>
                        <option value="ftc">FTC</option>
                        <option value="frc">FRC</option>
                    </select>
                </label>`;
    days.innerHTML += html;
}