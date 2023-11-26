function addDay() {
    var days = document.getElementById('teams');
    var number = days.children.length + 1;
    var html =
        `<br>
            <label>Team Number:
                <input type="text" pattern="\\d{1,5}" name="teamno${number}">
            </label>
            <br>
                <label>Team Type:
                    <select name="teamtype${number}">
                        <option value="fll">FLL</option>
                        <option value="ftc">FTC</option>
                        <option value="frc">FRC</option>
                    </select>
                </label>`;
    days.innerHTML += html;
}