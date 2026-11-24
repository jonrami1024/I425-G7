/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: AppRoutes.jsx
 * Description:
 */

import React from 'react';
import {BrowserRouter,Routes,Route}from "react-router-dom";
import Layout from "../components/Layout";
import Home from "../pages/home";
import NoMatch from "../pages/nomatch";
import Characters from "../pages/characters.jsx"
import Karts from "../pages/karts.jsx"
import Tires from "../pages/tires.jsx"
import Gliders from "../pages/gliders.jsx";
import Buildcalculator from "../pages/buildcalculator.jsx";
import Builds from "../pages/builds.jsx"
import Submitbuild from "../pages/submitbuild.jsx";
const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index element={<Home/>}/>
                    <Route path="*" element={<NoMatch/>}/>
                    <Route path="characters" element={<Characters/>}/>
                    <Route path="karts" element={<Karts/>}/>
                    <Route path="Tires" element={<Tires/>}/>
                    <Route path="Gliders" element={<Gliders/>}/>
                    <Route path="Buildcalculator" element={<Buildcalculator/>}/>
                    <Route path="Builds" element={<Builds/>}/>
                    <Route path="Submitbuild" element={<Submitbuild/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;