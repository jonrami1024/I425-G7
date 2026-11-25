/*
Name: Angel Avila
Date: 11/25/26
File: BuildRoutes.jsx
Description:
*/

import {Route} from 'react-router-dom';
import Builds from "../pages/builds/builds.jsx";
import Build from "../pages/builds/build.jsx";
import BuildStats from "../pages/builds/BuildStats.jsx";

const BuildRoutes = () => {
    return (
        <>
            <Route path="builds" element={<Builds/>}>
                <Route index element={<p>Select a build to view details.</p>}/>
                <Route path=":buildId" element={<Build/>}>
                    <Route index element={<BuildStats/>}/>
                    <Route path="stats" element={<BuildStats/>}/>
                </Route>
            </Route>
        </>
    );
};

export default BuildRoutes;