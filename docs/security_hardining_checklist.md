# CreatorOS AI Platform - Security Hardening Checklist

## Secrets Management

- [ ] No real API keys committed to GitHub
- [ ] `.env` is ignored by Git
- [ ] `.env.example` contains placeholders only
- [ ] Exposed Groq API key has been rotated
- [ ] Production secrets stored in Azure Key Vault or cloud secret manager

## API Security

- [ ] CORS restricted to trusted frontend domains
- [ ] Rate limiting enabled for public APIs
- [ ] Request validation enabled with Pydantic
- [ ] Unsafe input blocked by guardrails
- [ ] Error responses do not expose internal stack traces

## AI Safety

- [ ] Prompt injection checks enabled
- [ ] PII masking enabled
- [ ] Toxicity detection enabled
- [ ] Fact checking enabled
- [ ] Hallucination review enabled
- [ ] Human approval required before publishing

## Database Security

- [ ] PostgreSQL credentials stored outside code
- [ ] Database access restricted by environment
- [ ] Production database uses backups
- [ ] Least-privilege database user configured

## Frontend Security

- [ ] No secrets stored in React frontend
- [ ] API base URL configured through environment
- [ ] Sensitive actions require approval
- [ ] External links reviewed

## Production Security

- [ ] HTTPS enabled
- [ ] Authentication added before public deployment
- [ ] RBAC added for Admin, Creator, Reviewer
- [ ] Logs do not expose PII or secrets
- [ ] Monitoring alerts configured