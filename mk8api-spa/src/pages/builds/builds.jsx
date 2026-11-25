/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: Builds.jsx
 * Description:
 */

import {useState, useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import "/src/assets/css/build.css"
import {NavLink, Outlet, useLocation, useSearchParams} from "react-router-dom";
import Pagination from "./pagination.jsx"

const Builds = () => {
    const location = useLocation();
    const [subHeading, setSubHeading] = useState("All Builds");
    const [searchParams, setSearchParams] = useSearchParams();

    const {data, error, isLoading, abort, getAll}
        = useAxios('builds');
    const {meta, builds=[]} = data ?? {};

    useEffect(() => {
        if (!searchParams.get("limit") || !searchParams.get("offset")) {
            setSearchParams({
                limit: 10,
                offset: 0,
                sort: searchParams.get("sort") || "build_id"
            });
            return;
        }

        const params = Object.fromEntries(searchParams.entries());
        getAll(params);

        // Abort request if component unmounts
        return () => {
            abort();
        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [location.search]);

    return (
        <>
            <section className="content-box">
                <h2>Builds</h2>
                <hr/>
                <br/>
                <p>
                    {/* ill work on making this look more pretty - jonathan */}
                    Community made builds
                </p>
            </section>
            <section>
                <br/>
                <div className="sub-heading">
                    <div className="container">{subHeading}</div>
                </div>
                <div className="main-content container">
                    {error && <div>{error}</div>}
                    {isLoading &&
                        <div className="image-loading">
                            Please wait while data is being loaded
                        </div>}

                    {data && <div className="build-container">
                        <div className="build-list">
                            {builds.map((build) => (
                                <NavLink key={build.build_id}
                                         to={`/builds/${build.build_id}${location.search}`}
                                         className={({isActive}) =>
                                             isActive ? "active" : ""}>
                                    <span>&nbsp;</span>
                                    <div>{build.build_name}</div>
                                </NavLink>
                            ))}
                        </div>
                        <div className="build-item">
                            <Outlet context={[subHeading, setSubHeading]} />
                        </div>
                    </div>}

                    {meta && <Pagination meta={meta}/>}
                </div>
            </section>

        </>
    );
};

export default Builds;