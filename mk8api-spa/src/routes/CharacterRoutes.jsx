/*
Name: Angel Avila
Date: 11/25/26
File: CharacterRoutes.jsx
Description:
*/

import {Route} from 'react-router-dom';
import Characters from "../pages/character/characters.jsx";
import Character from "../pages/character/character.jsx";
import CharacterStats from "../pages/character/CharacterStats.jsx";

const CharacterRoutes = () => {
    return (
        <>
            <Route path="characters" element={<Characters/>}>
                <Route index element={<p>Select a character to view details.</p>}/>
                <Route path=":driverId" element={<Character/>}>
                    <Route index element={<CharacterStats/>}/>
                    <Route path="stats" element={<CharacterStats/>}/>
                </Route>
            </Route>
        </>
    );
};

export default CharacterRoutes;