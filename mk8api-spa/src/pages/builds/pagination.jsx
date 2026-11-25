/*
Name: Angel Avila
Date: 11/25/26
File: pagination.jsx
Description:
*/

import {Link, useNavigate} from "react-router-dom";

const Pagination = ({meta}) => {
    const navigate = useNavigate();
    const {limit, total_pages: totalPages, current_page: currentPage,
        next_page, previous_page, sort} = meta;

    const makePageUrl = (page) => {
        const currentPage = page && page > 0 ? page : 1;
        const offset = (currentPage - 1) * limit;
        let url = `/builds?limit=${limit}&offset=${offset}`

        if(sort) url += `&sort=${sort}`;

        return url;
    };

    const handleLimitChange = (e) => {
        const limit = Number(e.target.value);
        navigate(`/builds/?limit=${limit}&offset=0&sort=${sort || "build_id"}`);
    }

    const handleSortChange = (e) => {
        const sort = e.target.value;
        const search = location.search;

        let newSearch;
        if (search.includes("sort=")) {
            newSearch = search.replace(/sort=[^&]*/, `sort=${sort}`);
        } else {
            newSearch = search ? `${search}&sort=${sort}` : `?sort=${sort}`;
        }

        navigate(`${location.pathname}${newSearch}`);
    };

    return (
        <>
            {<div className="build-pagination-container">
                <div className="build-pagination">
                    Showing page {currentPage} of {totalPages}&nbsp;
                    <Link to={makePageUrl(1)}
                          title="First page"
                          className={currentPage === 1 ? "disabled" : ""}>&lt;&lt;
                    </Link>
                    <Link to={makePageUrl(previous_page)}
                          title="Previous page"
                          className={currentPage === 1 ? "disabled" : ""}>&lt;
                    </Link>
                    <Link to={makePageUrl(next_page)}
                          title="Next page"
                          className={next_page == null ? "disabled" : ""}>&gt;
                    </Link>
                    <Link to={makePageUrl(totalPages)}
                          title="Last page"
                          className={next_page == null ? "disabled" : ""}>&gt;&gt;
                    </Link>

                    &nbsp; Items per page &nbsp;
                    <select onChange={handleLimitChange} value={limit}>
                        {[5, 10, 15, 20].map((n) => (
                            <option key={n} value={n}>{n}</option>
                        ))}
                    </select>
                </div>
                <div className="build-sorting"> Sort by:&nbsp;
                    <select onChange={handleSortChange} value={sort || "build_id"}>
                        <option value="build_id">Build ID Ascending</option>
                        <option value="-build_id">Build ID Descending</option>
                        <option value="build_name">Name A-Z</option>
                        <option value="-build_name">Name Z-A</option>
                    </select>
                </div>
            </div>
            }
        </>
    );
};

export default Pagination;