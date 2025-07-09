
document.addEventListener("DOMContentLoaded", function() {
    const navItems = [
        { title: "Chain Of Thougt", href: "chain-of-thougt.html" },
        { title: "Chain Of Verification", href: "chain-of-verification.html" },
        { title: "Delimitadores", href: "delimitadores.html" },
        { title: "Dialogo Socratico", href: "dialogo-socratico.html" },
        { title: "Expert Interleaving", href: "expert-interleaving.html" },
        { title: "Generated Knowledge", href: "generated-knowledge.html" },
        { title: "Goal Oriented Planning", href: "goal-oriented-planning.html" },
        { title: "Json", href: "json.html" },
        { title: "Meta Prompt", href: "meta-prompt.html" },
        { title: "Pacef", href: "pacef.html" },
        { title: "Prompt Chaining", href: "prompt-chaining.html" },
        { title: "Rag", href: "rag.html" },
        { title: "React", href: "react.html" },
        { title: "Self Consistency", href: "self-consistency.html" },
        { title: "Self Critique E Self Refinement", href: "self-critique-e-self-refinement.html" },
        { title: "Skeleton Of Thought", href: "skeleton-of-thought.html" },
        { title: "Template Based Prompt", href: "template-based-prompt.html" },
        { title: "Tree Of Thougt", href: "tree-of-thougt.html" }
    ];

    const navbarHtml = `
        <a href="index.html">Home</a>
        <div class="dropdown">
            <a href="#" class="dropbtn">Técnicas &#9662;</a>
            <div class="dropdown-content">
                ${navItems.map(item => `<a href="${item.href}">${item.title}</a>`).join("")}
            </div>
        </div>
    `;

    const navbarContainer = document.querySelector(".navbar-placeholder");
    if (navbarContainer) {
        navbarContainer.innerHTML = navbarHtml;
    }
});


