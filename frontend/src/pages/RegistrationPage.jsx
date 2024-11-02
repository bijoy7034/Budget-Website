import React, { useState } from "react";
import { MDBInput, MDBBtn, MDBCard } from "mdb-react-ui-kit";

const RegistrationFormModel = {
  username: "",
  email: "",
  password: "",
  password2: "",
};

function RegistrationPage() {
  const [form, setForm] = useState(RegistrationFormModel);

  function handleChange(e) {
    const newForm = { ...form };
    newForm[e.target.id] = e.target.value;
    setForm(newForm);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    console.log(form);

    setForm(RegistrationFormModel);
  }

  return (
    <MDBCard>
      <form action="">
        <MDBInput
          className="mb-4"
          type="text"
          id="username"
          label="Username"
          value={form.username}
          onChange={handleChange}
        />
        <MDBInput
          className="mb-4"
          type="email"
          id="email"
          label="Email"
          value={form.email}
          onChange={handleChange}
        />
        <MDBInput
          className="mb-4"
          type="password"
          id="password"
          label="Password"
          value={form.password}
          onChange={handleChange}
        />
        <MDBInput
          className="mb-4"
          type="password"
          id="password2"
          label="Confirm Password"
          value={form.password2}
          onChange={handleChange}
        />
        <MDBBtn type="submit" block onClick={handleSubmit}>
          Register
        </MDBBtn>
      </form>
    </MDBCard>
  );
}

export default RegistrationPage;
