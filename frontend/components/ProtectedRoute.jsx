import { Navigate }from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import { ACCESS_TOKEN, REFRESH_TOKENS} from "../constants";
import { useState } from "react";
import api from "../api";

function ProtectedRoute({ children }) {
    const [isAuthenticated, setIsAuthenticated] = useState(null)

    const refreshTokens = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKENS)
        try {
            const response = await api.post("/api/token/refresh/",{ 
                refresh: refreshToken,
            })
        } catch (error) {
            console.error("Token refresh failed:", error)
            setIsAuthenticated(false)
        }
    }

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if(!token) {
            setIsAuthenticated(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenExp = decoded.exp
        const now = Date.now() / 1000

        if(tokenExp < now) {
            await refreshTokens()
        }
        else {
            setIsAuthenticated(true)
        }
    }

    if(isAuthenticated === null) {
        return <div>Loading...</div>
    }

    return isAuthenticated ? children : <Navigate to="/login" />

}