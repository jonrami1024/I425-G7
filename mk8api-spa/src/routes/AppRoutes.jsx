/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: AppRoutes.jsx
 * Description:
 */

import {BrowserRouter,Routes,Route}from "react-router-dom";
import Layout from "../components/Layout";
import Home from "../pages/home";
import NoMatch from "../pages/nomatch";
import CharacterRoutes from "./CharacterRoutes.jsx";
import Karts from "../pages/karts.jsx"
import Tires from "../pages/tires.jsx"
import Gliders from "../pages/gliders.jsx";
import Buildcalculator from "../pages/buildcalculator.jsx";
import BuildRoutes from "./BuildRoutes.jsx";
import Submitbuild from "../pages/submitbuild.jsx";

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index element={<Home/>}/>
                    <Route path="*" element={<NoMatch/>}/>
                    {CharacterRoutes()}
                    <Route path="karts" element={<Karts/>}/>
                    <Route path="Tires" element={<Tires/>}/>
                    <Route path="Gliders" element={<Gliders/>}/>
                    <Route path="Buildcalculator" element={<Buildcalculator/>}/>
                    {BuildRoutes()}
                    <Route path="Submitbuild" element={<Submitbuild/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;