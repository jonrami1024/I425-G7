/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: Layout.jsx
 * Description:
 */

import {Outlet} from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";

const Layout = () => {
    return (
        <>
            <Header />

            <br />

            <main>
                <section className="content-box">
                    <h2></h2>
                    <hr />
                    <Outlet />
                </section>
            </main>

            <Footer />
        </>
    );
};

export default Layout;