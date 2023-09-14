import { useState } from "react";
import Styles from "./FlagRegistration.module.css";


interface FlagRegistrationProps {
  handleClick: () => void;
}


const FlagRegistration = (props: FlagRegistrationProps) => {
  const [User, setUser] = useState('');
  const [Flag, setFlag] = useState('');

  const handleUserChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUser(event.target.value);
  };

  const handleFlagChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFlag(event.target.value);
  };

  const resetForm = () => {
      setUser("")
      setFlag("")
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log("User:", User);
    console.log("Flag:", Flag);
    props.handleClick()
    resetForm()

  };

  return (
    <>
      <div className={Styles.FlagRegistrationBackground}>
        <div className={Styles.FlagContainer}>
          <form onSubmit={handleSubmit}>
            <input type="text" value={User} onChange={handleUserChange} placeholder="Your name"/>
            <input type="text" value={Flag} onChange={handleFlagChange} placeholder="Enter flag"/>
              <input type="button" value="Close" onClick={props.handleClick}/>
              <input type="submit" value="Submit flag" />
          </form>
        </div>
      </div>
    </>
  );
};

export default FlagRegistration;
