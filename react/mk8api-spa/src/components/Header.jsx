
/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: Header.jsx
 * Description: create a common page header for MK8 API
 */

import {NavLink} from "react-router-dom";
import {Navbar, Nav, Container} from "react-bootstrap";
import logo from "../assets/img/logo.png";

const Header = () => {
    const className = ({ isActive }) => isActive ? "nav-link active" : "nav-link";

    return (
        <>
            <Navbar bg="dark" variant="dark" expand="lg">
                <Container>
                    <NavLink to="/" className="logo">
                        <Navbar.Brand>
                            <img src={logo} alt="MK8 API Logo" />
                        </Navbar.Brand>
                    </NavLink>

                    <Navbar.Toggle aria-controls="basic-navbar-nav" />

                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <NavLink to="/" className={className}>Home</NavLink>
                            <NavLink to="/characters" className={className}>Characters</NavLink>
                            <NavLink to="/karts" className={className}>Karts</NavLink>
                            <NavLink to="/tires" className={className}>Tires</NavLink>
                            <NavLink to="/gliders" className={className}>Gliders</NavLink>
                            <NavLink to="/Buildcalculator" className={className}>Build Calculator</NavLink>
                            <NavLink to="/builds" className={className}>Builds</NavLink>
                            <NavLink to="/Submitbuild" className={className}>Submit a Build</NavLink>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

export default Header;
