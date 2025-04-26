from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {
        "message": "Welcome to the Bdcalling Chatbot API!",
        "note": "This chatbot only responds to queries about Bdcalling IT Ltd.",
        "bdcalling": {
            "company": "Bdcalling IT Ltd.",
            "founded": "2013",
            "founder": "Muhammad Monir Hossain",
            "headquarters": "Dhaka, Bangladesh",
            "team_size": "900+ professionals",
            "global_reach": "47+ countries (USA, Canada, Australia, South Africa, Europe, etc.)",
            "core_services": {
                "BPO": "Inbound/outbound call center, data processing, virtual assistant support",
                "Web & Mobile Development": "Custom websites, UI/UX, mobile apps",
                "Odoo ERP Solutions": "Implementation and customization of Odoo ERP",
                "Digital Marketing": "SEO, SMM, telesales, strategy development",
                "Business Support": "Consultation, business setup, and strategic guidance"
            },
            "academy": {
                "name": "Bdcalling Academy",
                "launched": "July 2023",
                "description": "Skill development courses with scholarship and job opportunities"
            },
            "vision": "To be a global leader in IT services and contribute to Bangladesh's economic growth through technology"
        }
    }
