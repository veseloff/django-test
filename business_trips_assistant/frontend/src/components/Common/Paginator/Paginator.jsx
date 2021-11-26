import classes from "./Paginator.module.css";
import React from "react";
import cn from "classnames";

const Paginator = (props) => {
    const pagesCount = Math.ceil(props.count / props.pageSize);
    const pages = [];
    if (pagesCount !== 0) {
        pages.push('<');
        pages.push(1);
        if (pagesCount >= 2) {
            const min = Math.max(props.currentPage - 1, 2);
            const max = Math.min(props.currentPage + 1, pagesCount - 1);
            if (min !== 2)
                pages.push('...');
            for (let i = min; i <= max; i++)
                pages.push(i);
            if (max !== pagesCount - 1)
                pages.push('...');
            pages.push(pagesCount);
            pages.push('>');
        }
    }
    return (
        <div className={classes.pages}>
            {
                pages.length !== 0
                    ? pages.map((p, i) =>
                        <div key={i} className={cn({
                            [classes.selectedPage]: props.currentPage === p,
                            [classes.hoverPage]: !(p === '...'
                            || (p === '>' && props.currentPage === pagesCount || p === '<' && props.currentPage === 1)),
                        })}
                             onClick={() => {
                                 if (p !== '...' && p !== '>' && p !== '<')
                                     props.setCurrentPage(p);
                                 if (p === '>' && props.currentPage !== pagesCount) props.setCurrentPage(props.currentPage + 1);
                                 if (p === '<' && props.currentPage !== 1) props.setCurrentPage(props.currentPage - 1);
                             }}>
                            <span>{p}</span>
                        </div>)
                    : null
            }
        </div>
    )
}

export default Paginator;